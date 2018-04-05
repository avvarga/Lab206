function Node(val){ // class definition for Node
    this.value = val; // value is a property and val is the incoming value we want to set this.value to
    this.next = null; // next pointer is null as we don't assume the node have a buddy yet
}

function SLL(){ //class definition of SLL
    this.head = null; //head property set to null initially
    //AddFront function that adds a value, therefore node to the front of the SLL
    this.addFront = function(val){

        //create the node
        var node = new Node(val);
        // if the head of the SLL is empty, then we can simply set the head to the new node
        if (this.head == null){
            this.head = node;
        }
        // if the head is occupied, then create a temp to also point to the head so we can manipulate
        // the head to point elsewhere and not lose our previous head node
        // set the head to the new node, then set the new node's .next to the temp (previous head)
        else{
            var temp = this.head;
            this.head = node;
            node.next = temp;
        }
	}
	this.removeFront = function(){
		// determine if the list is empty or not
		if (this.head) { // if not empty
			var temp = this.head; // set a temp to the head node so we don't lose it after the next step
			this.head = this.head.next; // set the head to the head node's .next
			return temp.value; // return the temp's VALUE, not the entire node itself
		}
		return null; // if the list is empty, return null instead.
	}
    this.contains = function(val){
        var temp = this.head;
        while (temp != null){
            if (temp.value == val){
                return true;
            }
            temp = temp.next;
        }
        return false;
    }
    this.length=function(){
        var pointer=this.head;
        var length=0;
        while(pointer!=null){
            length++;
            pointer=pointer.next;
        }
        return length;
    }
    this.min=function(){
        if(this.head){
            var pointer=this.head.next;
            var min=this.head.value;
            while(pointer){
                if(pointer.value<min){
                    min=pointer.value;
                }
                pointer=pointer.next;
            }
            return min;
        }
        else{
            return undefined;
        }
    }
    this.max=function(){
        var pointer=this.head;
        var max=this.head.value;
        while(pointer){
            if(pointer.value>max){
                max=pointer.value;
            }
            pointer=pointer.next;
        }
        return max;
    }
}


var test=new SLL();
test.addFront(0);
test.addFront(6);
test.addFront(4);
test.addFront(2);
console.log(test);
console.log(test.max());