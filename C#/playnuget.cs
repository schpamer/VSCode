using System;
using Humanizer;

namespace playnuget
{
    class Program
    {
        static void Main(string[] args)
        {
            string answer;
            Console.WriteLine("Hello World!");
            answer = DateTime.UtcNow.AddHours(+34).Humanize();
            Console.WriteLine(answer);
        }
    }
}
