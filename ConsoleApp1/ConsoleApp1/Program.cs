using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;
using System.IO;    // for StreamReader
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            
            connect2();

        }
        

        public static void connect2()
        {
            var request = (HttpWebRequest)WebRequest.Create("http://localhost/hello.py");

            var postData = "data=hello";
            var data = Encoding.ASCII.GetBytes(postData);

            request.Method = "POST";
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = data.Length;

            using (var stream = request.GetRequestStream())
            {
                stream.Write(data, 0, data.Length);
            }
            try
            {
                var response = (HttpWebResponse)request.GetResponse();

                var responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
            }

            catch {; }


            
            
        }
    }
}
