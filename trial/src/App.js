import React, { Component } from "react";
import NavBar from "./components/navbar";
import "./App.css";

import Counters from "./components/counters";

class App extends Component {
	state = {
		counters: [
			{ id: 1, value: 4 },
			{ id: 2, value: 0 },
			{ id: 3, value: 0 },
			{ id: 4, value: 0 },
			{ id: 5, value: 0 }
		]
	};

	constructor() {
		super();
		console.log("App - Constructor");
	}

	componentDidMount() {
		console.log("App - Mounted");
	}

	handleIncrement = counter => {
		const counters = [...this.state.counters];
		const index = counters.indexOf(counter);
		counters[index] = { ...counter };
		counters[index].value++;
		this.setState({ counters });
	};

	handleDelete = counterID => {
		// console.log("Event handler called", counterID);
		const counters = this.state.counters.filter(c => c.id !== counterID);
		this.setState({ counters });
	};

	handleAdd = () => {
		const counters = [...this.state.counters];
		counters.push({ id: counters.length + 1, value: 0 });
		this.setState({ counters });
	};

	handleReset = () => {
		const counters = this.state.counters.map(c => {
			c.value = 0;
			return c;
		});
		this.setState({ counters });
	};

	render() {
		console.log("App - Rendered");
		return (
			<div>
				<NavBar
					totalCounters={this.state.counters.filter(c => c.value > 0).length}
				/>
				<main className="container">
					<Counters
						counters={this.state.counters}
						onReset={this.handleReset}
						onIncrement={this.handleIncrement}
						onDelete={this.handleDelete}
						onAdd={this.handleAdd}
					/>
				</main>
			</div>
		);
	}
}

export default App;
