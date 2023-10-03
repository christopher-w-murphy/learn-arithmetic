from time import sleep

from streamlit import set_page_config, markdown, title, selectbox, number_input, header, columns, button, empty


ops = {
    "Addition": "+",
    "Subtraction": "-",
    "Multiplication": "*"
}

special_answers = {
    100: ":100:"
}


def show_result(operation: str, result_time: int = 2) -> None:
    """
    Given an `operation`, show its result for `result_time` seconds.

    :param operation: The operation whose result we want to show
    :param result_time: How long to show the result for in seconds
    """
    result = empty()
    value = eval(operation)
    result.write(special_answers[value] if value in special_answers else value)
    sleep(result_time)
    result.empty()


def main(n_rows: int = 10, n_cols: int = 10) -> None:
    """
    :param n_rows: Number of rows to display
    :param n_cols: Number of columns to display
    """
    set_page_config(page_title="Learn Arithmetic!", page_icon=":1234:", layout="wide")

    markdown("<style> p { text-align: center; } </style>", unsafe_allow_html=True)

    title("Learn Arithmetic :heavy_plus_sign: :heavy_minus_sign: :heavy_multiplication_x:")

    op_col, idx_col, jdx_col = columns(3)
    with op_col:
        operator = selectbox("Select an operation", ops.keys())
    with idx_col:
        idx_0 = number_input("Row smallest value", min_value=-9, max_value=90, value=1, step=1)
    with jdx_col:
        jdx_0 = number_input("Column smallest value", min_value=-9, max_value=90, value=1, step=1)

    header(f"{operator} table:")

    for idx in range(idx_0, n_rows + idx_0):
        for jdx, col in enumerate(columns(n_cols), start=jdx_0):
            with col:
                operation = f"{idx}{ops[operator]}{jdx}"
                if button(f"${operation}$"):
                    show_result(operation)


if __name__ == '__main__':
    main()
