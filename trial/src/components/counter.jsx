import React, { Component } from "react";

class Counter extends Component {
	componentDidUpdate(prevProps, prevState) {
		console.log("prevProps", prevProps);
		console.log("prevState", prevState);
		if (prevProps.counter.value !== this.props.counter.value) {
			//Ajax call and get new data from the server
		}
	}

	componentWillUnmount() {
		console.log("Counter - On mount");
	}

	styles = {
		fontSize: 15,
		fontWeight: "bold"
	};

	render() {
		console.log("Counter - Rendered");
		return (
			<div>
				<span style={this.styles} className={this.getBadgeClasses()}>
					{this.formatCount()}
				</span>
				<button
					onClick={() => this.props.onIncrement(this.props.counter)}
					className="btn btn-secondary btn-sm"
				>
					Increment
				</button>
				<button
					onClick={() => this.props.onDelete(this.props.counter.id)}
					className="btn btn-danger btn-sm m-2"
				>
					Delete
				</button>
			</div>
		); //JSX component
	}

	// handleIncrement = () => {
	//   // console.log("Increment Clicked", this);
	//   this.setState({ value: this.state.value + 1 });
	// };

	getBadgeClasses() {
		let classes = "badge m-2 badge-";
		classes += this.props.counter.value === 0 ? "warning" : "primary";
		return classes;
	}

	formatCount() {
		const { value: count } = this.props.counter;
		return count === 0 ? "Zero" : count;
	}

	// renderTags() {
	//   if (this.state.tags.length === 0) return <p>There are no tags.</p>;
	//   return (
	//     <ul>
	//       {this.state.tags.map(tag => (
	//         <li key={tag}>{tag}</li>
	//       ))}
	//       {/* mapping string to JSX expression, similar to lazy coding  */}
	//     </ul>
	//   );
	// }
}

export default Counter;
