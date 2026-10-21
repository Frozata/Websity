class HTMLNode:
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props is None or self.props == {}:
			return ""
		attributes = ""
		for key, value in self.props.items():
			attributes += f' {key}="{value}"'
		return attributes
	def __repr__(self):
		return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
	def __init__(self, tag, value, props = None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError
		if self.tag is None:
			return self.value
		props_html = self.props_to_html()
		return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

	def __repr__(self):
		return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
	def __init__(self, tag, children, props = None):
		super().__init__(tag, None, children, props)
	def to_html(self):
		if self.tag is None:
			raise ValueError
		if self.children is None:
			raise ValueError("The children are lost")
		accumulate = ""
		props_html = self.props_to_html()
		for child in self.children:
			accumulate += child.to_html()
		return f'<{self.tag}{props_html}>{accumulate}</{self.tag}>'



