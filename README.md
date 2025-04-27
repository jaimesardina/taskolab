# About the project

Taskolab is a centralized automation platform that empowers support teams to run predefined engineering-approved tasks across distributed infrastructure. 

## About Me and Taskolab
In every workplace I have worked at, I notice there were gaps with engineers and support or even non IT people. Of course this is the norm and we never question it. After all, why would we trust the project manager or sales guy to patch and reboot a server... Ok lets not get in trouble with HR but really, our support team would be able to take care of this using a system that templates this. Have worked in environments where I was the only IT person in a small business to a corporate environment I noticed the gap never went away. More resources does not always solve efficiency. Im not an expert in software development, I have a background in support and networking. However in the past 4 years I have spent time consistently automating tasks using batch files, python, and now picking up Go. I am comitted to creating such a tool that can be accessible to small or large enterprices. I am a network engineer full time so bare with me, I work on this project outside my work, volunteer work in my beliefs, and improving my software engineering skills. 

## Current status of this project
Taskolab is in very.. very.. **early development**.  
However I will share that this project has a **working foundation** that includes:

- Backend FastAPI server with secure JWT authentication
- Dynamic backend mapper system to control agent behavior
- Modular, organized logic template system for operations, menus, and automation scripts
- CLI agent prototype capable of:
  - Authenticating to backend
  - Fetching dynamic instructions from the server
  - Importing and executing dynamic logic templates

## Features
- Lightweight CLI agent for remote execution
- Centralized task definition and control
- Modular design with React-based frontend (To Be implemented)

## Taskolab aims to provide:
- Full backend-driven orchestration of agents
- Modular task templates and automation scripts
- Support for hierarchical menus and branching workflows
- Centralized logic and dictionary management
- Dynamic agent behavior without redeploying agents
- Fine-grained control based on user roles (developer, support, etc.)

## Roadmap Objectives
- Backend Security Enhancements
- Add sub-mapper support for deeper multi-layer menus
- Develop full web-based management dashboard with modern GUI look (React + Tailwind) (tbd)
- Role-based access control for users
- Error handling and audit logging
- Various testing

## License
MIT License with Commons Clause (See license for more detils)