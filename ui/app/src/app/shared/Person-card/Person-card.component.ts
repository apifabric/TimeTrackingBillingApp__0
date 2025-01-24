import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Person-card.component.html',
  styleUrls: ['./Person-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Person-card]': 'true'
  }
})

export class PersonCardComponent {


}