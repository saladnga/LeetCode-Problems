class Node {
public:
    int val;
    Node* next;
    Node(int val): val(val), next(nullptr) {}
};
class MyLinkedList {
public:
    Node* head;
    int size;
    MyLinkedList(): head(nullptr), size(0) {}
    
    int get(int index) {
        if (index >= size || index < 0) {
            return -1;
        }
        Node* current = head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        return current->val;
    }
    
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    void addAtIndex(int index, int val) {
        if (index > size || index < 0) {
            return;
        }
        Node* new_node = new Node(val);
        if (index == 0) {
            new_node->next = head;
            head = new_node;
        }
        else {
            Node* current = head;
            for (int i = 0; i < index - 1; i++) {
                current = current->next;
            }
            new_node->next = current->next;
            current->next = new_node;
        }
        size += 1;
    }
    
    void deleteAtIndex(int index) {
        if (index >= size || index < 0) {
            return;
        }
        if (index == 0) {
            Node* temp = head;
            head = head->next;
        }
        else {
            Node* current = head;
            for (int i = 0; i < index - 1; i++) {
                current = current->next;
            }
            Node* temp = current->next;
            current->next = current->next->next;
            delete temp;
        }
        size = size - 1;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */