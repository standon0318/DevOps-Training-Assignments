

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace project.Controllers
{
[Route("api/[controller]")]
    public class app2Controller : Controller
    {
[HttpGet]
 public string Get()
        {
            return "Good Morning";
        }
}
}


