package guis;

import org.lwjgl.util.vector.Vector2f;

public class GuiTexture {
	private int texture;
	private Vector2f position;
	private Vector2f scale;
	
	
	public GuiTexture(int loadTexture, Vector2f position2, Vector2f scale2) {
		// TODO Auto-generated constructor stub
		super();
		this.texture = texture;
		this.position = position;
		this.scale = scale;
	}
	public int getTexture() {
		return texture;
	}
	public Vector2f getPosition() {
		return position;
	}
	public Vector2f getScale() {
		return scale;
	}
	
	
}
