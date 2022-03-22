import { Component, OnInit } from '@angular/core';
import { DockerService } from './_service/docker.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'frontDockerManager';
  containers: any;
  state: boolean;
  container: {id: string, name: string};

  constructor(private dockerService: DockerService){
    this.state = false;
    this.container = {
      'id': '',
      'name': ''
    }
  }

  ngOnInit(){
    this.dockerService.getAll().subscribe(
      response => {
        this.containers = response;
      },
      error => {
        console.log(error)
      }
    );
  }

  changeState(){
    if(this.state == true){
      this.state = false;
    } else if(this.state == false){
      this.state = true;
    }
  }

  addContainer(){
    this.dockerService.add(this.container.id, this.container.name).subscribe(
      response => {
        location.reload()
      },
      error => {
        console.log(error)
      }
    );
  }

  start(id: string){
    this.dockerService.start(id).subscribe(
      response => {},
      error => {
        console.log(error)
      }
    );
  }

  stop(id: string){
    this.dockerService.stop(id).subscribe(
      response => {},
      error => {
        console.log(error)
      }
    );
  }

  pause(id: any){
    this.dockerService.pause(id).subscribe(
      response => {},
      error => {
        console.log(error)
      }
    );
  }

  unpause(id: string){
    this.dockerService.unpause(id).subscribe(
      response => {},
      error => {
        console.log(error)
      }
    );
  }

  delete(id: string){
    this.dockerService.delete(id).subscribe(
      response => {
        location.reload()
      },
      error => {
        console.log(error)
      }
    );
  }
}
