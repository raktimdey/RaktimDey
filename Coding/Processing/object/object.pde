int y=100; 
int dy=5;
void setup(){
 size(500,500); 
  
}
void draw(){
  background(155);
  ellipse(200,y,50,50);
  y=y+dy;
  if(y+25>width||y-25<0){
    dy= dy*-1;
}
}