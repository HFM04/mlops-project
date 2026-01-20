def test_environment_and_dependencies():
    import sys
    import numpy as np

    # Basic sanity: running on Python 3
    assert sys.version_info.major == 3

    # Dependency pin validation
    assert np.__version__ == "1.24.3"
