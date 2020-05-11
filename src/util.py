def filter_templates(code, filter_by):
	return code.filter_templates(matches=lambda t: t.name.matches(filter_by))


def template_params_to_dict(template):
	template_dict = {}
	for param in template.params:
		name = str.strip(param.name.get(0).value)
		value = str.strip(param.value.get(0).value)
		if name and value:
			template_dict[name] = value
	return template_dict

