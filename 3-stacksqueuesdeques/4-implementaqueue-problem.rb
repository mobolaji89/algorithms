class Queue

  def initialize
    @items = []
  end

  def is_empty?
    @items.empty?
    # OR @items == []
  end

  def enqueue(item)
    @items.unshift(item)
    # OR @items.insert(0, item)
  end

  def dequeue
    @items.pop
  end

  def size
    @items.length
  end

end
