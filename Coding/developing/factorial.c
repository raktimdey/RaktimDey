factorial(int n);
void main(){
	
	int s;
	s=factorial(6);
	printf("%d",s);
	getch();
	
}
factorial(int n){
	int f;
	if(n==1){
	
	return 1;
	}
	else{
	
	n*factorial(n-1);
}
	return f;
}
