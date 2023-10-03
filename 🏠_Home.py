from streamlit import set_page_config, title, markdown


def main() -> None:
    set_page_config(page_title="Learn Arithmetic!", page_icon=":house:")

    title("Learn Arithmetic!")

    markdown("**:point_left: Select a game from the sidebar** and starting playing!")


if __name__ == '__main__':
    main()
