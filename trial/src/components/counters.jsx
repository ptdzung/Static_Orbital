import React, { Component } from "react";
import Counter from "./counter";
class Counters extends Component {
	render() {
		console.log("Counters - Rendered");

		const { onReset, counters, onDelete, onIncrement, onAdd } = this.props;
		return (
			<div>
				<button onClick={onReset} className="btn btn-primary btn-small m-2">
					Reset
				</button>
				<button onClick={onAdd} className="btn btn-success btn-small m-2">
					Addition
				</button>
				{counters.map(counter => (
					<Counter
						key={counter.id}
						onDelete={onDelete}
						onIncrement={onIncrement}
						counter={counter}
					/>
				))}
			</div>
		);
	}
}

export default Counters;
