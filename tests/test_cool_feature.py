import pytest
import numpy as np
import pandas as pd


@pytest.mark.parametrize("dtype", ["int8", "int16", "int32", "int64"])
def test_dtypes(dtype):
    assert str(np.dtype(dtype)) == dtype


@pytest.mark.parametrize(
    "dtype",
    [
        "float32",
        pytest.param("int16", marks=pytest.mark.skip),
        pytest.param("int32", marks=pytest.mark.xfail(reason="to show how it works")),
    ],
)
def test_mark(dtype):
    assert str(np.dtype(dtype)) == "float32"


@pytest.fixture
def series():
    return pd.Series([1, 2, 3])


@pytest.fixture(params=["int8", "int16", "int32", "int64"])
def dtype(request):
    return request.param


def test_series(series, dtype):
    result = series.astype(dtype)
    assert result.dtype == dtype

    expected = pd.Series([1, 2, 3], dtype=dtype)
    pd.testing.assert_series_equal(result, expected)
