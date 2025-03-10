# global
import tensorflow as tf
from tensorflow.python.types.core import Tensor
import typing

# local
import ivy


def expm1(x: Tensor)\
        -> Tensor:
    return tf.math.expm1(x)


def bitwise_invert(x: Tensor)\
        -> Tensor:
    if 'int' not in str(x.dtype):
        return tf.logical_not(x)
    return tf.bitwise.invert(x)


def bitwise_and(x1: Tensor,
                x2: Tensor)\
        -> Tensor:
    return tf.bitwise.bitwise_and(x1, x2)


def ceil(x: Tensor)\
        -> Tensor:
    if 'int' in str(x.dtype):
        return x
    return tf.math.ceil(x)


def floor(x: Tensor)\
        -> Tensor:
    if 'int' in str(x.dtype):
        return x
    return tf.math.floor(x)


def isfinite(x: Tensor) \
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.ones_like(x, tf.bool)
    return tf.math.is_finite(x)


def asin(x: Tensor) \
        -> Tensor:
    return tf.asin(x)


def isinf(x: Tensor) \
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.zeros_like(x, tf.bool)
    return tf.math.is_inf(x)


def _tf_cast(x: Tensor, dtype: tf.dtypes.DType) -> Tensor:
    try:
        return tf.cast(x, dtype)
    except ValueError:
        return x


def _cast_for_binary_op(x1: Tensor, x2: Tensor)\
        -> typing.Tuple[typing.Union[Tensor, int, float, bool], typing.Union[Tensor, int, float, bool]]:
    x1_bits = ivy.functional.backends.tensorflow.old.general.dtype_bits(x1.dtype)
    if isinstance(x2, (int, float, bool)):
        return x1, x2
    x2_bits = ivy.functional.backends.tensorflow.old.general.dtype_bits(x2.dtype)
    if x1_bits > x2_bits:
        x2 = _tf_cast(x2, x1.dtype)
    elif x2_bits > x1_bits:
        x1 = _tf_cast(x1, x2.dtype)
    return x1, x2


def equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.math.equal(x1, x2)


def less_equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.math.less_equal(x1, x2)


def asinh(x: Tensor) \
        -> Tensor:
    return tf.asinh(x)


def sqrt(x: Tensor)\
        -> Tensor:
    if x.dtype == 'float32':
        x_64 = tf.cast(x, tf.float64)
        return tf.cast(tf.sqrt(x_64), x.dtype)
    return tf.math.sqrt(x)


def cosh(x: Tensor) \
        -> Tensor:
    return tf.cosh(x)


def log10(x: Tensor) \
        -> Tensor:
    return tf.experimental.numpy.log10(x)


def log(x: Tensor)\
        -> Tensor:
    return tf.math.log(x)


def log2(x: Tensor) \
        -> Tensor:
    return tf.experimental.numpy.log2(x)


def log1p(x: Tensor) \
        -> Tensor:
    return tf.experimental.numpy.log1p(x)


def isnan(x: Tensor)\
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.zeros_like(x, tf.bool)
    return tf.math.is_nan(x)


def less(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.math.less(x1, x2)


def cos(x: Tensor)\
        -> Tensor:
    return tf.cos(x)


def logical_not(x: Tensor)\
        -> Tensor:
    return tf.logical_not(tf.cast(x, tf.bool))


def greater_equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.math.greater_equal(x1, x2)


def acos(x: Tensor)\
        -> Tensor:
    return tf.acos(x)


def logical_xor(x1: Tensor, x2: Tensor) \
        -> Tensor:
    return tf.math.logical_xor(tf.cast(x1, tf.bool), tf.cast(x2, tf.bool))


def logical_or(x1: Tensor, x2: Tensor)\
        -> Tensor:
    return tf.logical_or(tf.cast(x1, tf.bool), tf.cast(x2, tf.bool))


def logical_and(x1: Tensor, x2: Tensor)\
        -> Tensor:
    return tf.logical_and(tf.cast(x1, tf.bool), tf.cast(x2, tf.bool))


def acosh(x: Tensor) \
        -> Tensor:
    return tf.acosh(x)


def sin(x: Tensor)\
        -> Tensor:
    return tf.sin(x)


def negative(x: Tensor) -> Tensor:
    if x.dtype in [tf.uint8, tf.uint16, tf.uint32, tf.uint64]:
        return tf.cast(tf.negative(tf.cast(x, tf.float32)), x.dtype)
    return tf.negative(x)


def not_equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.math.not_equal(x1, x2)


def tanh(x: Tensor) \
        -> Tensor:
    return tf.tanh(x)


def sinh(x: Tensor) \
        -> Tensor:
    return tf.sinh(x)


def bitwise_or(x1: Tensor, x2: Tensor) \
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return x1 | x2


def positive(x: Tensor)\
        -> Tensor:
    return tf.experimental.numpy.positive(x)


def square(x: Tensor)\
        -> Tensor:
    return tf.math.square(x)


def remainder(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.experimental.numpy.remainder(x1, x2)


def round(x: Tensor)\
        -> Tensor:
    if 'int' in str(x.dtype):
        return x
    return tf.round(x)


def abs(x: Tensor)\
        -> Tensor:
    return tf.math.abs(x)


def subtract(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.subtract(x1, x2)


def logaddexp(x1: Tensor, x2: Tensor) -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.experimental.numpy.logaddexp(x1, x2)


tan = tf.tan


def atan(x: Tensor) \
        -> Tensor:
    return tf.atan(x)


atan2 = tf.atan2
cosh = tf.math.cosh
atanh = tf.math.atanh
log = tf.math.log
exp = tf.math.exp

# Extra #
# ------#


erf = tf.math.erf
