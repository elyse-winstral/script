import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import anywidget
    import traitlets
    return anywidget, mo, traitlets


@app.cell
def _(anywidget, mo, traitlets):
    class ConditionalProbWidget(anywidget.AnyWidget):
        _esm = """
        import interact from "https://cdn.jsdelivr.net/npm/interactjs/+esm";

        function createSquare(model, el, id) {
            const container = el.querySelector("#container");
            const square = document.createElement("div");
            const label = document.createElement("span");
            label.textContent = id.toUpperCase();
            label.style.position = "absolute";
            label.style.top = "5px";
            label.style.left = "5px";
            label.style.fontWeight = "bold";
            square.appendChild(label);

            let w = model.get(`width_${id}`);
            let h = model.get(`height_${id}`);
            square.style.width = `${w}px`;
            square.style.height = `${h}px`;
            square.style.border = `2px solid ${id === 'a' ? 'steelblue' : 'firebrick'}`;
            square.style.backgroundColor = id === 'a' ? 'lightblue' : 'lightcoral';
            square.style.opacity = "0.7";
            square.style.touchAction = "none";
            square.style.userSelect = "none";
            square.style.position = "absolute";

            let x = model.get(`x_${id}`);
            let y = model.get(`y_${id}`);
            square.style.transform = `translate(${x}px, ${y}px)`;

            container.appendChild(square);

            interact(square)
                .draggable({
                    listeners: {
                        move(event) {
                            x += event.dx;
                            y += event.dy;
                            event.target.style.transform = `translate(${x}px, ${y}px)`;
                            model.set(`x_${id}`, x);
                            model.set(`y_${id}`, y);
                            model.save_changes();
                        },
                    },
                    modifiers: [
                        interact.modifiers.restrictRect({
                            restriction: 'parent',
                            endOnly: true
                        })
                    ]
                })
                .resizable({
                    edges: { left: true, right: true, bottom: true, top: true },
                    listeners: {
                        move: function (event) {
                            w = event.rect.width;
                            h = event.rect.height;

                            x = (x || 0) + event.deltaRect.left;
                            y = (y || 0) + event.deltaRect.top;

                            event.target.style.width = `${w}px`;
                            event.target.style.height = `${h}px`;
                            event.target.style.transform = `translate(${x}px, ${y}px)`;

                            model.set(`width_${id}`, w);
                            model.set(`height_${id}`, h);
                            model.set(`x_${id}`, x);
                            model.set(`y_${id}`, y);
                            model.save_changes();
                        },
                    },
                    modifiers: [
                        interact.modifiers.restrictSize({
                            min: { width: 20, height: 20 },
                            max: { width: 400, height: 400 },
                        }),
                        interact.modifiers.restrictRect({
                            restriction: 'parent',
                            endOnly: true
                        })
                    ],
                });
        }

        function render({ model, el }) {
            const container = document.createElement("div");
            container.id = "container";
            container.style.width = "300px";
            container.style.height = "300px";
            container.style.border = "1px solid #ccc";
            container.style.position = "relative";
            container.style.overflow = "hidden";

            const omegaLabel = document.createElement("div");
            omegaLabel.textContent = "Ω";
            omegaLabel.style.position = "absolute";
            omegaLabel.style.top = "5px";
            omegaLabel.style.right = "10px";
            omegaLabel.style.fontSize = "24px";
            omegaLabel.style.color = "#ccc";
            container.appendChild(omegaLabel);

            el.appendChild(container);

            createSquare(model, el, 'a');
            createSquare(model, el, 'b');
        }
        export default { render };
        """
        x_a = traitlets.Float(33).tag(sync=True)
        y_a = traitlets.Float(16.5).tag(sync=True)
        width_a = traitlets.Float(150).tag(sync=True)
        height_a = traitlets.Float(150).tag(sync=True)

        x_b = traitlets.Float(98).tag(sync=True)
        y_b = traitlets.Float(66.5).tag(sync=True)
        width_b = traitlets.Float(170).tag(sync=True)
        height_b = traitlets.Float(200).tag(sync=True)

    prob_widget = mo.ui.anywidget(ConditionalProbWidget())
    return (prob_widget,)


@app.cell
def _(mo):
    mo.md("""
    # Conditional Probability: $P(A|B)$

    Drag and resize squares $A$ and $B$ to see how the conditional probability $P(A|B)$ changes. The default $A$ and $B$ represent independent events: $P(A|B) = P(A)$. Note, independence is not restricted to this specific configuration.
    """)
    return


@app.cell
def _(mo, prob_widget):
    # Calculate areas
    area_a = prob_widget.width_a * prob_widget.height_a
    area_b = prob_widget.width_b * prob_widget.height_b

    # Calculate intersection area
    x_intersect = max(prob_widget.x_a, prob_widget.x_b)
    y_intersect = max(prob_widget.y_a, prob_widget.y_b)

    x_right_a = prob_widget.x_a + prob_widget.width_a
    y_bottom_a = prob_widget.y_a + prob_widget.height_a
    x_right_b = prob_widget.x_b + prob_widget.width_b
    y_bottom_b = prob_widget.y_b + prob_widget.height_b

    w_intersect = max(0, min(x_right_a, x_right_b) - x_intersect)
    h_intersect = max(0, min(y_bottom_a, y_bottom_b) - y_intersect)

    area_intersect = w_intersect * h_intersect

    # Calculate conditional probability P(A|B)
    p_a_given_b = area_intersect / area_b if area_b > 0 else 0

    # Display results
    results = mo.md(f"""
        ### Probabilities
        - **P(A):** {(area_a / (300*300)):.3f}
        - **P(B):** {(area_b / (300*300)):.3f}
        - **P(A ∩ B):** {(area_intersect / (300*300)):.3f}
    """)

    # Visualization for P(A|B)
    prob_bar_html = f"""
    <div style="border: 1px solid #ccc; padding: 10px; margin-top: 0px; width: 100%;">
        <h4 style="margin-top: 0;">Conditional Probability P(A|B)</h4>
        <div style="font-family: monospace; font-size: 14px;">
            P(A|B) = Area(A ∩ B) / Area(B) = <strong>{p_a_given_b:.3f}</strong>
        </div>
        <div style="margin-top: 10px; background-color: #f0f0f0; border-radius: 5px; padding: 5px;">
            <div style="background-color: lightcoral; width: 100%; height: 30px; border: 1px solid firebrick; position: relative; border-radius: 3px; overflow: hidden;">
                <div style="background-color: steelblue; opacity: 0.6; width: {p_a_given_b * 100}%; height: 100%; position: absolute; top: 0; left: 0;"></div>
                <span style="position: absolute; left: 5px; top: 5px; color: white; font-weight: bold; text-shadow: 1px 1px 2px #333;">
                    Area(B)
                </span>
                 <span style="position: absolute; right: 5px; top: 5px; color: white; font-weight: bold; text-shadow: 1px 1px 2px #333;">
                    100%
                </span>
            </div>
            <div style="text-align: center; margin-top: 5px; font-size: 12px;">The shaded area represents the proportion of B that is also A.</div>
        </div>
    </div>
    """

    #mo.hstack([results, mo.Html(prob_bar_html)], justify="space-around")
    mo.hstack([prob_widget, mo.vstack([mo.Html(prob_bar_html), results], align='start')], justify="start")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Probability and area

    When building an understanding of probability theory, it can be very helpful to picture the probability as the area. Probability and area (Lebesgue measure, denoted $\lambda(\cdot)$) are both metrics- probability *measures* the chance of an event occuring. There is even a special case where the two metrics are identical:

    Let $\Omega = [0,1] \times [0,1]$ be the unit square. The Lebesgue measure of $\Omega$ is $\lambda(\Omega) = (1-0)\cdot(1-0) = 1$. Let $\mathcal{F} = \mathcal{B}([0,1] \times [0,1])$ and $\mathbb{P}$ the uniform probability measure over $\mathcal{F}$. So for our probability space $(\Omega, \mathcal{F}, \mathbb{P})$ the probability of any event in that space is its area:

    Put plainly, for $A \in \mathcal{F}$, $\mathbb{P}(A) =$ Area$(A) = \lambda(A)$.
    """)
    return


if __name__ == "__main__":
    app.run()
