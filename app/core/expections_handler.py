from fastapi.responses import JSONResponse
from fastapi import HTTPException, Request


async def handle_exceptions(request: Request, exc: Exception):
    exception_type = type(exc)

    if exception_type is ArithmeticError:
        return await handle_arithmetic_error(request, exc)  # type: ignore
    elif exception_type is AttributeError:
        return await handle_attribute_error(request, exc)  # type: ignore
    elif exception_type is HTTPException:
        return await handle_http_exception(request, exc)  # type: ignore
    else:
        return await handle_generic_exception(request, exc)


async def handle_arithmetic_error(request: Request, exc: ArithmeticError):
    return JSONResponse(
        status_code=400,
        content={"error": "ArithmeticError occurred", "detail": str(exc)},
    )


async def handle_attribute_error(request: Request, exc: AttributeError):
    return JSONResponse(
        status_code=400,
        content={"error": "AttributeError occurred", "detail": str(exc)},
    )


async def handle_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": f"HTTPException occurred - {exc.detail}",
                 "detail": str(exc)},
    )


async def handle_generic_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Unhandled Exception occurred", "detail": str(exc)},
    )
