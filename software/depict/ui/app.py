

from __future__ import annotations


def main() -> None:
    try:
        import streamlit as st
    except ImportError:  # pragma: no cover
        raise SystemExit("Install the UI extra: pip install -e 'software[ui]'")

    st.set_page_config(page_title="DEPict", page_icon="🔬")
    st.title("DEPict — microplastic polymer ID")
    st.caption("Tri-modal sensing: DEP · EIS · CV, fused on-device.")


    st.info("Scaffold UI — wire up acquisition + plots here.")


if __name__ == "__main__":
    main()
