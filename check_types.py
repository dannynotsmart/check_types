from functools import wraps
from inspect import signature


def check_if_correct_type(arg, parameter):
	annotation = parameter.annotation

	if annotation is parameter.empty or type(arg) == annotation or isinstance(
			arg, annotation):
		return True

	return False


def check_types(func):
	@wraps(func)
	def check_type(*args, **kwargs):
		sig = signature(func)

		if len(sig.parameters) == 0:
			return func(*args, **kwargs)

		parameters = sig.parameters
		bind = sig.bind(*args, **kwargs)

		for name in bind.arguments:
			arg = bind.arguments.get(name)
			parameter = parameters[name]
			annotation = parameter.annotation

			result = check_if_correct_type(arg, parameter)

			if result is False:
				raise TypeError(
					'Value "{0}" at argument "{1}" is an incorrect annotation. Should be {2}, or a child'.
					format(arg, name, annotation))

		return func(*args, **kwargs)

	return check_type
