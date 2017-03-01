class Stack
  def initialize
    @items = []
  end

  def is_empty?
    @items.empty?
    # OR @items = []
  end

  def push(item)
    @items.push(item)
  end

  def pop
    @items.pop
  end

  def peek
    @items.last
    # OR @items[-1] in Ruby
    # OR @new_stack[@new_stack.length - 1] seen in other languages
  end

  def size
    @items.length
  end
end
