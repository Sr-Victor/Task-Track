#include <iostream>
#include <string>
#include <fstream>
#include <random>
// CLI Task Manager



using namespace std;
int main(){
  cout << "Please, select a option: " << endl << endl;
  cout << "1 - Add task" << endl;
  cout << "2 - Remove task" << endl;
  cout << "3 - Update Task" << endl;
  cout << "4 - List all tasks" << endl;
  cout << "5 - List all tasks that are done" << endl;
  cout << "6 - List all tasks that are not done" << endl;
  cout << "7 - List all tasks that are in progress" << endl;
  cout << endl;
  int opt;
  cout << "--> :"; cin >> opt;


  /* 
    id: A unique identifier for the task
    description: A short description of the task
    status: The status of the task (todo, in-progress, done)
    createdAt: The date and time when the task was created
    updatedAt: The date and time when the task was last updated
  */


  switch (opt)
  {
  case 1:
    cout << "OK, What's task name?";
    
    string taskName;
    cout << "--> : "; cin >> taskName;
    break;

  case 2:
    cout << "";
    break; 
    
  case 3:
    cout << "";
    break;
  
  case 4:
    cout << "";
    break;

  case 5:
    cout << "";
    break;

  case 6:
    cout << "";
    break;

  default:
    break;
  }
  return 0;
}