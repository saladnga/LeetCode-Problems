class MovingAverage {
public:

    int maxSize;
    queue<int> queue;
    double sum;

    MovingAverage(int size) {
        this->maxSize = size;
        this->sum = 0.0;
    }
    
    double next(int val) {
        if (queue.size() == maxSize) {
            sum -= queue.front();
            queue.pop();
        }
        sum += val;
        queue.push(val);
        return sum / queue.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */