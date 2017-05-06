int x=100; //x axis....if you want to use y axis change it y
int dx=5;
void setup(){
 size(500,500); 
  
}
void draw(){
  background(155);
  ellipse(x,200,50,50);
  x=x+dx;
  if(x+25>width||x-25<0){
    dx= dx*-1;
}
}