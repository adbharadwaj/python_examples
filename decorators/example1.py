def decorator(inner):
	def inner_decorator(*args, **kwargs):
		print('before')
		inner(*args, **kwargs)
		print('after')
	return inner_decorator


@decorator
def decorated(num):
	print('%s %s' % ('foo', num))

if __name__ == '__main__':
	decorated(1)
