class Deque
  def initialize
    @items = []
  end

  def is_empty?
    @items.empty?
    # OR @items == []
  end

  def add_front(item)
    @items.push(item)
  end

  def add_rear(item)
    @items.unshift(item)
    # OR @items.insert(0, item)
  end

  def remove_front
    @items.shift
    # OR @items.pop(0)
  end

  def remove_rear
    @items.pop
  end
end
