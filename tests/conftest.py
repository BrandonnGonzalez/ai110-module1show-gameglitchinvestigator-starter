import sys
import os
from unittest.mock import MagicMock

# Ensure the project root is on the path so imports like `logic_utils` and `app` resolve
# regardless of where pytest is invoked from.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Stub out streamlit so app.py can be imported without a running Streamlit server.
st_mock = MagicMock()
st_mock.session_state = MagicMock()
st_mock.session_state.__contains__ = lambda self, key: True  # treat all keys as present

# sidebar.selectbox must return a real string so attempt_limit_map[difficulty] doesn't fail.
st_mock.sidebar.selectbox.return_value = "Normal"

# st.columns(n) must return an iterable of n items for tuple unpacking to work.
st_mock.columns.side_effect = lambda n: [MagicMock() for _ in range(n)]

sys.modules["streamlit"] = st_mock
