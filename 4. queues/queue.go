package main

type Queue []interface{}

func (s *Queue) enqueue(item interface{}) {
	*s = append(*s, item)
}

func (s *Queue) dequeue() interface{} {
	if len(*s) == 0 {
		return nil
	}

	item := (*s)[0]
	*s = (*s)[1:]
	return item
}

func (s *Queue) peek() interface{} {
	if len(*s) == 0 {
		return nil
	}

	return (*s)[0]
}

func (s *Queue) isEmpty() bool {
	return len(*s) == 0
}

func (s *Queue) addToQueue(arr []interface{}) {
	for i := 0; i < len(arr); i++ {
		s.enqueue(arr[i])
	}
}
