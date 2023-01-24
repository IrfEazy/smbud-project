<!--
    Improved compatibility of back to a top link: See:
    https://github.com/othneildrew/Best-README-Template/pull/73
-->

<a name="readme-top"></a>

<!--
    *** Thanks for checking out the Best-README-Template. If you have a suggestion
    *** that would make this better, please fork the repo and create a pull request
    *** or simply open an issue with the tag "enhancement".
    *** Don't forget to give the project a star!
    *** Thanks again! Now go create something AMAZING! :D
-->

<!--
    *** I'm using markdown "reference style" links for readability.
    *** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
    *** See the bottom of this document for the declaration of the reference variables
    *** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
    *** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors](https://img.shields.io/github/contributors/IrfEazy/smbud-project.svg?style=for-the-badge)](https://github.com/IrfEazy/smbud-project/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/IrfEazy/smbud-project.svg?style=for-the-badge)](https://github.com/IrfEazy/smbud-project/network/members)
[![Stargazers](https://img.shields.io/github/stars/IrfEazy/smbud-project.svg?style=for-the-badge)](https://github.com/IrfEazy/smbud-project/stargazers)
[![Issues](https://img.shields.io/github/issues/IrfEazy/smbud-project.svg?style=for-the-badge)](https://github.com/IrfEazy/smbud-project/issues)
[![MIT License](https://img.shields.io/github/license/IrfEazy/smbud-project.svg?style=for-the-badge)](https://github.com/IrfEazy/smbud-project/blob/main/LICENSE)

<br/>
<div style="text-align: center">
    <a href="https://github.com/IrfEazy/smbud-project">
        <img src="images/logo.ico" alt="Logo" width="80" height="80">
    </a>
    <h3 style="text-align: center">Systems and Methods for Big and Unstructured Data</h3>
    <p>
        Project of Systems and Methods for Big and Unstructured Data.
        <br/>
        <a href="https://github.com/IrfEazy/smbud-project">
            <strong>Explore the docs »</strong>
        </a>
        <br/>
        <br/>
        <a href="https://github.com/IrfEazy/smbud-project">View Demo</a>
        ·
        <a href="https://github.com/IrfEazy/smbud-project/issues">Report Bug</a>
        ·
        <a href="https://github.com/IrfEazy/smbud-project/issues">Request Feature</a>
    </p>
</div>
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#about-the-project">About The Project</a>
            <ul>
                <li>
                    <a href="#built-with">Built With</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li>
                    <a href="#prerequisites">Prerequisites</a>
                </li>
                <li>
                    <a href="#installation">Installation</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#usage">Usage</a>
        </li>
        <li>
            <a href="#contributing">Contributing</a>
        </li>
        <li>
            <a href="#license">License</a>
        </li>
        <li>
            <a href="#contact">Contact</a>
        </li>
    </ol>
</details>

## About The Project

The purpose of the project is to create a bibliographic database, namely a system able to store and manage data
regarding scientific articles and all their meaningful characteristics and relations with authors and the place where
they are published.

* implementation in Neo4j
* implementation in MongoDB
* implementation in PySpark

### Neo4j

The main dataset used can be downloaded from the site [www.aminer.org](https://www.aminer.org/citation), in particular,
the latest version of data was employed, namely DBLP-Citation network V13. The dataset was not entirely imported in
Neo4j because it was huge and our machines with limited computing power were not able to handle it, so just a part of it
was taken, containing information about 2315 papers.

This [link](https://github.com/IrfEazy/smbud-project/blob/main/neo4j/queries.cyp) collects in a file the queries of the
main document.

### MongoDB

Each scientific paper has a full description of document structure and content as

* Title, Abstract, Authors (with affiliations, email, bio)
* Metadata (keywords)
* Publication details (journal, volume, number, date, pages)
* Sections: title, text (by paragraph), subsections, figures (image URL and caption)
* Bibliography (set of refs.)

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section lists any major frameworks/libraries used to bootstrap the project.

* ![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)
* ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
* ![Neo4J](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* Install Neo4j
   ```shell
   ./install-neo4j.sh
   ```
* Install MongoDB
  ```shell
  ./install-mongodb.sh
  ```
* Run Mongo-Shell by launching `mongosh` command in the terminal, and then create Administrative MongoDB User
  ```shell
  use admin
  ```
  ```shell
  db.createUser({
    user: "username",
    pwd: "password",
    roles: [{
      role: "userAdminAnyDatabase",
      db: "admin"
    }]
  })
  ```
  ```shell
  quit()
  ```
    * To test the changes, access the mongo shell using the created administrative user.
      ```shell
      mongosh -u username -p --authenticationDatabase admin
      ```
* Download and extract the dataset
   ```shell
   wget https://originalstatic.aminer.cn/misc/dblp.v13.7z
   7z x dblpv13.7z
   ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't
rely on any external dependencies or services._

1. Clone the repo
    ```shell
    git clone https://github.com/IrfEazy/smbud-project.git
    ```

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos
work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Irfan Cela - [LinkedIn](https://linkedin.com/in/irfan-cela-1511b3244) - irfan.cela@mail.polimi.it

Fabio Lusha - [LinkedIn](https://www.linkedin.com/in/fabio-lusha-816410252/) - fabio.lusha@mail.polimi.it

Alberto Sandri - [LinkedIn](https://www.linkedin.com/in/alberto-sandri-780264166/) - alberto.sandri@mail.polimi.it

Bianca Christiana Savoiu Marinas - [LinkedIn](https://www.linkedin.com/in/bianca-savoiu-0766bb191/) -
biancachristiana.savoiu@mail.polimi.it

Enrico Simionato - [LinkedIn](https://www.linkedin.com/in/enrico-simionato-5791b919b/) - enrico.simionato@mail.polimi.it

Project Link: [https://github.com/IrfEazy/smbud-project](https://github.com/IrfEazy/smbud-project)

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>