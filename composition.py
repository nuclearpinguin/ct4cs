# 2. Implement the composition function in your favorite language.
# It takes two functions as arguments and returns 
# a function that is their composition.
from inspect import signature


def evaluate(f, args):
	"""
	Evaluates function for given arguments
	"""
	arg_no = len(list(signature(f).parameters))
	if arg_no == 1:
		return f(args)
	elif isinstance(args, tuple):
		return f(*args)
	elif isinstance(args, dict):
		return f(**args)
	else:
		raise ValueError


def compose(f, g):
	"""
	Creates composition of two functions. Double evaluation
	allows to use the simple left and right identity:
	id = lambda x: x
	"""
	return lambda args : evaluate(f, (evaluate(g, args)))


if __name__ == '__main__':
	# Test 1
	a = lambda x: x + 2
	b = lambda x: x + 4
	c = compose(a, b)

	print('a(x) = x + 2')
	print('b(x) = x + 4')
	print('c(x) = g(f(x)) , c(0) = ', c(0))

	print('\n--------------')

	# Test 2
	f = lambda x, y: x + y
	g = lambda x: x + 2
	c = compose(g, f)

	print('f(x, y) = x + y')
	print('g(x) = x + 2')
	print('c(x, y) = g(f(x, y)) , c(1,2) = ', c((1,2)))

	print('\n--------------')

	# Test 3
	print('c(x, y) = g(f(x, y)) , c({y:1, x:2}) = ', c({'y':1, 'x':2}))
