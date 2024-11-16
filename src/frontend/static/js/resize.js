const RESIZE_HANDLES = {
    "right-resize": { width: 1, x: 0 },
    "left-resize": { width: -1, x: 1 },
    "bottom-resize": { height: 1, y: 0 },
    "top-resize": { height: -1, y: 1 },
    "bottom-right-resize": { width: 1, height: 1, x: 0, y: 0 },
    "bottom-left-resize": { width: -1, height: 1, x: 1, y: 0 },
    "top-right-resize": { width: 1, height: -1, x: 0, y: 1 },
    "top-left-resize": { width: -1, height: -1, x: 1, y: 1 },
};

class WindowResizer {
    constructor() {
        this.isResizing = false;
        this.state = {
            handle: null,
            startX: 0,
            startY: 0,
            startWidth: 0,
            startHeight: 0,
            startWindowX: 0,
            startWindowY: 0,
            minWidth: 0,
            minHeight: 0,
        };

        this.startResize = this.startResize.bind(this);
        this.resize = this.resize.bind(this);
        this.stopResize = this.stopResize.bind(this);

        this.init();
    }

    async init() {
        document.querySelectorAll(".resize-handle").forEach((handle) => {
            handle.addEventListener("mousedown", this.startResize, { passive: true });
        });
    }

    async startResize(e) {
        this.isResizing = true;
        this.state.handle = RESIZE_HANDLES[e.target.id];

        if (!this.state.handle) return;

        this.state.startX = e.screenX;
        this.state.startY = e.screenY;

        const [size, pos, minSize] = await Promise.all([
            window.pywebview.api.window.size(),
            window.pywebview.api.window.position(),
            window.pywebview.api.window.min_size(),
        ]);

        Object.assign(this.state, {
            startWidth: size.width,
            startHeight: size.height,
            startWindowX: pos.x,
            startWindowY: pos.y,
            minWidth: minSize.width,
            minHeight: minSize.height,
        });

        document.addEventListener("mousemove", this.resize, { passive: true });
        document.addEventListener("mouseup", this.stopResize, { passive: true });
        e.preventDefault();
    }

    resize(e) {
        if (!this.isResizing) return;

        const dx = e.screenX - this.state.startX;
        const dy = e.screenY - this.state.startY;
        const handle = this.state.handle;

        let newDimensions = {
            width: this.state.startWidth + (handle.width ? dx * handle.width : 0),
            height: this.state.startHeight + (handle.height ? dy * handle.height : 0),
            x: this.state.startWindowX + (handle.x ? dx : 0),
            y: this.state.startWindowY + (handle.y ? dy : 0),
        };

        if (newDimensions.width < this.state.minWidth) {
            if (handle.x) {
                newDimensions.x = this.state.startWindowX + (this.state.startWidth - this.state.minWidth);
            }
            newDimensions.width = this.state.minWidth;
        }

        if (newDimensions.height < this.state.minHeight) {
            if (handle.y) {
                newDimensions.y = this.state.startWindowY + (this.state.startHeight - this.state.minHeight);
            }
            newDimensions.height = this.state.minHeight;
        }

        requestAnimationFrame(() => {
            window.pywebview.api.window.resize(
                newDimensions.width,
                newDimensions.height,
                newDimensions.x,
                newDimensions.y
            );
        });
    }

    stopResize() {
        this.isResizing = false;
        document.removeEventListener("mousemove", this.resize);
        document.removeEventListener("mouseup", this.stopResize);
    }
}

const windowResizer = new WindowResizer();
