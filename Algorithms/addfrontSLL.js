// addFront(val)

function Node(val){
    this.val = val;
    this.next = null;
}

functionSLL(){
    this.head = val;
    this.addFront = function(val){
        var node = new Node (val);
        if (this.head == null){
            this.head=node;
        }
        else{
            node.next = this.head;
            this.head = node;
        }
    }
    this.removeFront = function (){
        if (this.head == null){
            return null
        }
        else{
            var temp = this.head;
            this.head = temp.next;
            temp = null;
        }
    }
    return this.head;
}



