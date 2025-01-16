"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean
from inflammation.models import daily_max
from inflammation.models import daily_min

@pytest.mark.parametrize(
    "test, expect",
    [
        ( [[0, 0],[0, 0],[0, 0]], [0, 0] ),
        ( [[1, 2],[3, 4],[5, 6]], [3, 4] ),
    ])
def test_daily_mean_with_different_inputs(test, expect):
    """ test daily mean with different inputs"""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expect))


@pytest.mark.parametrize(
    "test, expect",
    [
        ( [[0, 0],[0, 0],[0, 0]], [0, 0] ),
        ( [[1, 2],[3, 4],[5, 6]], [5, 6] ),
    ])
def test_daily_max_with_different_inputs(test, expect):
    """ test daily max with different inputs"""
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expect))

    
@pytest.mark.parametrize(
    "test, expect",
    [
        ( [[0, 0],[0, 0],[0, 0]], [0, 0] ),
        ( [[1, 2],[3, 4],[5, 6]], [1, 2] ),
    ])
def test_daily_min_with_different_inputs(test, expect):
    """ test daily min with different inputs"""
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expect))


def test_wrong_input():
    """test for typerror"""

    with pytest.raises(TypeError):
        error_expected = daily_mean([["A","B"],["C","D"]])