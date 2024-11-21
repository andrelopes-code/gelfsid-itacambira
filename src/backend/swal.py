import json


def _execute_swal(window, function_name, *args):
    args_str = json.dumps(args)[1:-1]
    result = window.evaluate_js(f'SwalUtils.{function_name}({args_str})')
    return result


def success(
    window,
    message,
    title='SUCESSO',
):
    return _execute_swal(
        window,
        'success',
        message,
        title,
    )


def error(
    window,
    message,
    title='UM ERRO OCORREU',
):
    return _execute_swal(
        window,
        'error',
        message,
        title,
    )


def confirm(
    window,
    message,
    title='CONFIRMAÇÃO',
    confirm_text='Sim',
    cancel_text='Não',
):
    return _execute_swal(
        window,
        'confirm',
        message,
        title,
        confirm_text,
        cancel_text,
    )


def warning(
    window,
    message,
    title='ATENÇÃO',
):
    return _execute_swal(
        window,
        'warning',
        message,
        title,
    )


def toast(
    window,
    message,
    icon='success',
    position='top-end',
):
    return _execute_swal(
        window,
        'toast',
        message,
        icon,
        position,
    )


def loading(
    window,
    message='Carregando...',
):
    return _execute_swal(
        window,
        'loading',
        message,
    )


def prompt(
    window,
    message,
    title='Digite',
    input_placeholder='',
):
    return _execute_swal(
        window,
        'prompt',
        message,
        title,
        input_placeholder,
    )


def html(
    window,
    html_content,
    title='',
):
    return _execute_swal(
        window,
        'html',
        html_content,
        title,
    )


def delete(
    window,
    message='Esta ação não poderá ser revertida!',
    title='Tem certeza?',
):
    return _execute_swal(
        window,
        'delete',
        message,
        title,
    )


def auto_close(
    window,
    message,
    title='',
    timer=2000,
):
    return _execute_swal(
        window,
        'autoClose',
        message,
        title,
        timer,
    )


def close(window, self):
    window.evaluate_js('Swal.close()')
