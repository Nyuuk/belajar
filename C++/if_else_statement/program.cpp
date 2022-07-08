#include <iostream>
#include <string>
//#include <sstream>

using namespace std;

string kinyuk(){
  return false;
}

bool kunyuk(){
  return "";
}

int main(){
  bool a;
  //istringstream(kunyuk()) >> a;
  //cout << a << endl;
  if (kunyuk()){
    cout << "Kunyuk Benar" << endl;
  } else {
    cout << "Kunyuk Salah" << endl;
  }
//  if (kinyuk()){
//    cout << "kinyuk True" << endl;
//  }else {
//    cout << "kinyuk False" << endl;
//  }
  cout << "kinyuk: " << kinyuk << endl;
  return 0;
}
