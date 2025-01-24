import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Task-card.component.html',
  styleUrls: ['./Task-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Task-card]': 'true'
  }
})

export class TaskCardComponent {


}