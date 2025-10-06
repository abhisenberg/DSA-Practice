package main

func revQueue(queue *Queue) {
	if queue.isEmpty() {
		return
	}

	item := queue.dequeue()
	revQueue(queue)
	queue.enqueue(item)
}
