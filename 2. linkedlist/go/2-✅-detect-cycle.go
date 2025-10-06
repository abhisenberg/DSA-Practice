package main

/*
Problem statements:
https://leetcode.com/problems/linked-list-cycle/
https://leetcode.com/problems/linked-list-cycle-ii/
*/

/*
Cycle detection and first node of the loop detection
https://www.youtube.com/watch?v=Cs3KwAsqqn4

Detecting first node of the loop:
Method: Collisions and Mathematical Reasoning

    Collision Point: After detecting the loop, keep the 'fast' pointer at the point of collision within the loop.
		Let's call this point 'P'.
    Reset 'slow':  Initialize the 'slow' pointer back to the head of the list.
    Synchronized Movement:  Start moving both the 'slow' and 'fast' pointers forward, this time at the same pace (one node at a time).
    Guaranteed Meeting:  The point where the 'slow' and 'fast' pointers meet next is the first node of the loop.

Why Does This Work?

Let's revisit the earlier notation:
    L: Distance from the list's head to the start of the loop.
    C: Length of the loop cycle.
    P: Our meeting point inside the loop. Let's say it's 'm' distance away from the beginning of the loop within the cycle,
		i.e., after L + m the cycle pattern repeats.

Analysis:
    When the 'slow' pointer is reset to the head, the 'fast' pointer is within the cycle.
	From the meeting point 'P', it still needs to cover a distance of (C - m) to complete a full loop
		and return to the loop's starting point.
    While the 'fast' pointer completes the remaining distance (C - m) of its current cycle,
		the 'slow' pointer will cover distance 'L' from the head.
    As both pointers move at the same pace, they are destined to meet exactly at the start of the cycle.

*/

//Part 1
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	slow, fast := head, head

	for {
		if slow == nil || fast == nil || fast.Next == nil {
			return false
		}

		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			return true
		}
	}

	return false
}

//Part 2
func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	slow, fast := head, head

	for {
		if slow == nil || fast == nil || fast.Next == nil {
			return nil
		}

		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			break
		}
	}

	/*
	   - Put the slow pointer back to the list head
	   - Move both slow and fast pointer at the same speed
	   - The point where they meet is the starting of the loop
	*/
	slow = head
	for slow != fast {
		slow = slow.Next
		fast = fast.Next
	}

	return slow

}
