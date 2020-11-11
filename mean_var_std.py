import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  matrix = np.array(list).reshape((3, 3))

  means = [
    # axis1
    matrix.mean(axis=0).tolist(),
    # axis2
    matrix.mean(axis=1).tolist(),
    # flattened
    matrix.mean().tolist()
  ]

  variances = [
    # axis1
    np.var(matrix, axis=0).tolist(),
    # axis2
    np.var(matrix, axis=1).tolist(),
    # flattened
    np.var(matrix).tolist()
  ]

  standard_deviations = [
    # axis1
    np.std(matrix, axis=0).tolist(),
    # axis2
    np.std(matrix, axis=1).tolist(),
    # flattened
    np.std(matrix).tolist()
  ]

  maxes = [
    # axis1
    matrix.max(axis=0).tolist(),
    # axis2
    matrix.max(axis=1).tolist(),
    # flattened
    matrix.max().tolist()
  ]

  mins = [
    # axis1
    matrix.min(axis=0).tolist(),
    # axis2
    matrix.min(axis=1).tolist(),
    # flattened
    matrix.min().tolist()
  ]

  sums = [
    # axis1
    matrix.sum(axis=0).tolist(),
    # axis2
    matrix.sum(axis=1).tolist(),
    # flattened
    matrix.sum().tolist()
  ]

  return {
    'mean': means,
    'variance': variances,
    'standard deviation': standard_deviations,
    'max': maxes,
    'min': mins,
    'sum': sums
  }