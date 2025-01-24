import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Client-card.component.html',
  styleUrls: ['./Client-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Client-card]': 'true'
  }
})

export class ClientCardComponent {


}