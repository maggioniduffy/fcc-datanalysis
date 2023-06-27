import numpy as np


def get_means(matrix):
  return [matrix.mean(0), matrix.mean(1), matrix.mean()]


def get_variances(matrix):
  return [matrix.var(0), matrix.var(1), matrix.var()]


def get_std_dev(matrix):
  return [matrix.std(0), matrix.std(1), matrix.std()]


def get_max(matrix):
  return [matrix.max(0), matrix.max(1), matrix.max()]


def get_mins(matrix):
  return [matrix.min(0), matrix.min(1), matrix.min()]


def get_sums(matrix):
  return [matrix.sum(0), matrix.sum(1), matrix.sum()]


def calculate(list):
  print(len(list))
  if (len(list) != 9):
    raise ValueError('List must contain nine numbers.')

  aux = np.array(list)
  matrix = aux.reshape((3, 3))

  mean = get_means(matrix)
  vars = get_variances(matrix)
  std = get_std_dev(matrix)
  max = get_max(matrix)
  min = get_mins(matrix)
  sum = get_sums(matrix)

  calculations = {
    'mean': mean,
    'variance': vars,
    'standard deviation': std,
    'max': max,
    'min': min,
    'sum': sum,
  }
  return calculations
