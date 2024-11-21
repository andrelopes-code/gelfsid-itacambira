class ContextMenu {
    constructor() {
        this.menu = document.getElementById("context-menu");
        this.lastClickedElement = null;

        this.executePaste = this.executePaste.bind(this);
        this.executeCopy = this.executeCopy.bind(this);
        this.executeCut = this.executeCut.bind(this);

        this.menuItems = [
            {
                id: "paste",
                label: "Colar",
                icon: "icon-paste",
                shortcut: "Ctrl+V",
                action: this.executePaste,
                condition: (element) => element.tagName === "INPUT" || element.tagName === "TEXTAREA",
            },
            {
                id: "copy",
                label: "Copiar",
                icon: "icon-copy",
                shortcut: "Ctrl+C",
                action: this.executeCopy,
                condition: (element) => window.getSelection().toString().length > 0,
            },
            {
                id: "cut",
                label: "Recortar",
                icon: "icon-cut",
                shortcut: "Ctrl+X",
                action: this.executeCut,
                condition: (element) => window.getSelection().toString().length > 0,
            },
        ];

        this.setupEventListeners();
    }

    setupEventListeners() {
        document.addEventListener("contextmenu", this.handleContextMenu.bind(this));
        document.addEventListener("click", this.handleClick.bind(this));
        document.addEventListener("keydown", this.handleKeyDown.bind(this));
    }

    handleContextMenu(e) {
        e.preventDefault();
        this.lastClickedElement = e.target;
        this.menu.innerHTML = "";
        const relevantItems = this.menuItems.filter((item) =>
            item.condition ? item.condition(this.lastClickedElement) : true
        );

        if (relevantItems.length === 0) {
            this.menu.classList.add("hidden");
            return;
        }

        relevantItems.forEach((item, index) => {
            const menuItem = this.createMenuItem(item);
            if (index < relevantItems.length - 1) {
                menuItem.classList.add("border-b", "border-gray-100");
            }
            this.menu.appendChild(menuItem);
        });

        const x = Math.min(e.pageX, window.innerWidth - this.menu.offsetWidth);
        const y = Math.min(e.pageY, window.innerHeight - this.menu.offsetHeight);

        this.menu.classList.remove("hidden");
        this.menu.style.left = `${x}px`;
        this.menu.style.top = `${y}px`;
    }

    createMenuItem(item) {
        const div = document.createElement("div");
        div.className = "flex items-center px-4 py-2 hover:bg-gray-50 cursor-pointer select-none";

        const iconTemplate = document.getElementById(item.icon);
        const icon = iconTemplate.cloneNode(true);
        icon.classList.remove("hidden");

        const textContainer = document.createElement("div");
        textContainer.className = "flex justify-between items-center flex-1 ml-3";

        const label = document.createElement("span");
        label.className = "text-gray-700";
        label.textContent = item.label;

        const shortcut = document.createElement("span");
        shortcut.className = "text-gray-400 text-sm ml-4";
        shortcut.textContent = item.shortcut;

        textContainer.appendChild(label);
        textContainer.appendChild(shortcut);

        div.appendChild(icon);
        div.appendChild(textContainer);

        div.addEventListener("click", () => {
            item.action();
            this.hide();
        });

        return div;
    }

    handleClick(e) {
        if (!this.menu.contains(e.target)) {
            this.hide();
        }
    }

    handleKeyDown(e) {
        if (e.key === "Escape") {
            this.hide();
        }
    }

    hide() {
        this.menu.classList.add("hidden");
    }

    async executePaste() {
        if (!this.lastClickedElement) return;

        try {
            const text = await pywebview.api.clipboard.get();
            const start = this.lastClickedElement.selectionStart;
            const end = this.lastClickedElement.selectionEnd;

            const currentValue = this.lastClickedElement.value;
            this.lastClickedElement.value =
                currentValue.substring(0, start) + text + currentValue.substring(end);

            const newPos = start + text.length;
            this.lastClickedElement.setSelectionRange(newPos, newPos);

            this.lastClickedElement.dispatchEvent(new Event("input", { bubbles: true }));
        } catch (err) {
            console.error("error pasting:", err);
        }
    }

    executeCopy() {
        const text = window.getSelection().toString();
        if (text) {
            pywebview.api.clipboard.set(text);
        }
    }

    executeCut() {
        const text = window.getSelection().toString();
        if (text) {
            pywebview.api.clipboard.set(text);
            if (
                this.lastClickedElement.tagName === "INPUT" ||
                this.lastClickedElement.tagName === "TEXTAREA"
            ) {
                const start = this.lastClickedElement.selectionStart;
                const end = this.lastClickedElement.selectionEnd;
                this.lastClickedElement.value =
                    this.lastClickedElement.value.substring(0, start) +
                    this.lastClickedElement.value.substring(end);
                this.lastClickedElement.setSelectionRange(start, start);
            }
        }
    }
}

const contextMenu = new ContextMenu();
