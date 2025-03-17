struct Node {
    int val;
    Node* next;
    Node(int val) : val(val), next(nullptr) {}
};

class MyLinkedList {
public:
    Node* head;
    MyLinkedList() {
        head = nullptr;
    }
    
    int get(int index) {
        int count = 0;
        Node* temp = head;
        while (temp != nullptr) {
            count++;
        }
        if (count == index) {
            return temp->val;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        Node* newHead = new Node(val);
        newHead->next = head;
        head = newHead;
    }
    
    void addAtTail(int val) {
        Node* temp = head;
        Node* newNode = new Node(val);
        while (temp->next != nullptr) {
            if (temp == nullptr) {
                head->next = newNode;
            }
            head = head->next;
        }
    }
    
    void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }
        Node* temp = head;
        int count = 0;
        while (count < index && temp != nullptr) {
            temp = temp->next;
            count++;
        }
        if (temp == nullptr) {
            return;
        }
        Node* newNode = new Node(val);
        newNode->next = temp->next;
        temp->next = newNode;
    }
    
    void deleteAtIndex(int index) {
        if (head == nullptr) {
            return;
        }
        int count = 0;
        Node* temp = head;
        while (count < index && temp != nullptr) {
            temp = temp->next;
            count++;
        }
        if (temp == nullptr) {
            return;
        }
        Node* nodeToDelete = temp->next;
        temp->next = nodeToDelete->next;
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