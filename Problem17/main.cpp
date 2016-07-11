#include <unordered_map>
#include <iostream>
#include <cstdlib>

int number_length(int number);
#define MAX_VALUE 1000
std::unordered_map<int,int> intmap({{0,0},{1,3},{2,3},{3,5},{4,4},{5,4},{6,3},{7,5},{8,5},{9,4},{10,3},{11,6},{12,6},{13,8},{14,8},{15,7},{16,7},{17,9},{18,8},{19,8},{20,6},{30,6},{40,5},{50,5},{60,5},{70,7},{80,6},{90,6},{100,7},{1000,8}});
int main(int argc, char * argv[])
{
/*	for(auto i= intmap.begin(); i!= intmap.end();i++){
		std::cout<<i->first<< "  --- " <<i->second << std::endl;
	}
	std::cout<<number_length(1)<<std::endl;
	std::cout<<number_length(21)<<std::endl;
	std::cout<<number_length(200)<<std::endl;
	* 
	* */
	int letters = 0;
	int stop = 1000;
	std::cout<<"Twenty " <<number_length(20)<<std::endl;
	if(argc == 2)
		stop = int(atoi(argv[1])) + 1;
	for(int i=1; i<stop;i++){
		letters += number_length(i);
	}
	
	std::cout<<"Letters from 1 to "<<stop<< " is "<<letters<<std::endl;
	//std::cout<<number_length(342)<<std::endl;
}

int number_length(int n){
	int result = 0;
	int number = n;
	if (number >= 1000)
	{
		result += intmap.find(number/1000)->second + intmap.find(1000)->second;
		number %= 1000; 
	}
	if(number >= 100){
		result += intmap.find(number/100)->second + intmap.find(100)->second;
	//	std::cout<<"100"<<std::endl;
	}
	if (number >100 && number %100 != 0){
		result += 3; //for and
		//std::cout<<"10"<<std::endl;
	}
	if(number%100 > 19){
		result += intmap.find(((number%100)/10)*10)->second + intmap.find(number%10)->second;
		//std::cout<<"11111111"<<std::endl;
	}
	if(number%100 <20 && number%100 != 0){
		result += intmap.find(number%100)->second;
		//std::cout<<"0"<<std::endl;
	}
	return result;
}
