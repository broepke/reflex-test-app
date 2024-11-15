import reflex as rx

def my_button():
    return rx.button("Click Me")

def my_page():
    return rx.box(
        rx.text("This is a page"),
        # Reference components defined in other functions.
        my_button(),
    )