using System;
using System.Collections.Generic;
using System.Text;

public class StuffManager
{
    private string Customer_Name; 
    public readonly string Account_Number; 

    public StuffManager(string accNum)
    {
        Account_Number = accNum;
    }

    public void DoStuff(string user_name) 
    {
        string customer_name = "Jane Smith"; 
        
        Customer_Name = customer_name;
        
        if (customer_name != null)
        {
            Console.WriteLine($"Processing data for {customer_name}");
        }
    }
}

public class MyProgram
{
    public static void Main()
    {
        StuffManager my_manager = new StuffManager("12345"); 
        my_manager.DoStuff("Jane Doe");
    }
}