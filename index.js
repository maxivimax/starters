#! /usr/bin/env node

import inquirer from 'inquirer';
import * as fs from 'fs';
import { addicionalQuestions } from './addicionalQuestions.js';

import { fileURLToPath } from 'url';
import { dirname } from 'path';
import fse from 'fs-extra';

const __filename = fileURLToPath(import.meta.url);
const __dirnameStarter = dirname(__filename) + "/starters";

const questions = [
  {
    type: "list",
    name: "projectType",
    message: "Please, select starter",
    choices: fs.readdirSync(__dirnameStarter, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name.charAt(0).toUpperCase() + d.name.slice(1)),
    filter(val) {
      return val.toLowerCase();
    },
  },
  {
    type: "input",
    name: "projectName",
    message: "Please enter your new project's name.",
    default: "newProject"
  },
]

const confirmQuestion = [
  {
    type: "confirm",
    name: "sureCheck",
    message: "You are sure?",
  }
]

function copyStarter(projectName, projectType) {
  inquirer.prompt(confirmQuestion).then(answers => {
    const { sureCheck } = answers;

    if (sureCheck) {
      if (fs.existsSync("./" + projectName)) {
        console.log("\nDirectory \"" + projectName + "\" alredy exist.")
        return false
      } else {
        try {
          fse.copySync(__dirnameStarter + "/" + projectType, "./" + projectName, { overwrite: false })

          console.log("\n")
          console.log(projectType.charAt(0).toUpperCase() + projectType.slice(1) + ' project success created with \"Maxivimax Starters\"!\nThank you for using!')

          return true
        } catch (err) {
          console.error(err)
          return false
        }
      }
    } else {
      console.log("It's so sad... See you later!")
    }
  })
}

console.log("Hello!\nIt's a \"Maxivimax Starters\"!\n")

inquirer.prompt(questions).then(answers => {
  const { projectName, projectType } = answers;

  if (projectType in addicionalQuestions) {
    inquirer.prompt(addicionalQuestions[projectType]).then(answers => {
      switch (projectType) { }

      copyStarter(projectName, projectType)
    })
  } else {
    copyStarter(projectName, projectType)
  }
})