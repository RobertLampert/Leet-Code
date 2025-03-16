//   Definition for singly-linked list.
var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
    return ListNode;
}());
function mergeTwoLists(list1, list2) {
    console.log(list1);
    return list1;
}
;
// Create individual nodes
var node1 = new ListNode(10); // A node with value 10
var node2 = new ListNode(20); // A node with value 20
var node3 = new ListNode(30); // A node with value 30
// Link the nodes to form a list
node1.next = node2; // node1 points to node2
node2.next = node3; // node2 points to node3
node3.next = null; // node3 is the last node, so it points to null
mergeTwoLists(node1, node1);
