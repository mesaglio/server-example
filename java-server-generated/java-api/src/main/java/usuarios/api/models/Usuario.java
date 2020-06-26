package usuarios.api.models;

import java.util.Objects;

import org.springframework.validation.annotation.Validated;

import com.fasterxml.jackson.annotation.JsonProperty;

import io.swagger.annotations.ApiModelProperty;

/**
 * Usuario
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2020-06-25T18:07:03.789-03:00[America/Buenos_Aires]")
public class Usuario {
	@JsonProperty("documento")
	private String documento = null;

	@JsonProperty("username")
	private String username = null;

	@JsonProperty("nombres")
	private String nombres = null;

	@JsonProperty("apellidos")
	private String apellidos = null;

	@JsonProperty("genero")
	private String genero = null;

	@JsonProperty("fechaNacimiento")
	private String fechaNacimiento = null;

	public Usuario documento(String documento) {
		this.documento = documento;
		return this;
	}

	/**
	 * Get documento
	 * @return documento
	 **/
	@ApiModelProperty(value = "")

	public String getDocumento() {
		return documento;
	}

	public void setDocumento(String documento) {
		this.documento = documento;
	}

	public Usuario username(String username) {
		this.username = username;
		return this;
	}

	/**
	 * Get username
	 * @return username
	 **/
	@ApiModelProperty(value = "")

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public Usuario nombres(String nombres) {
		this.nombres = nombres;
		return this;
	}

	/**
	 * Get nombres
	 * @return nombres
	 **/
	@ApiModelProperty(value = "")

	public String getNombres() {
		return nombres;
	}

	public void setNombres(String nombres) {
		this.nombres = nombres;
	}

	public Usuario apellidos(String apellidos) {
		this.apellidos = apellidos;
		return this;
	}

	/**
	 * Get apellidos
	 * @return apellidos
	 **/
	@ApiModelProperty(value = "")

	public String getApellidos() {
		return apellidos;
	}

	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}

	public Usuario genero(String genero) {
		this.genero = genero;
		return this;
	}

	/**
	 * Get genero
	 * @return genero
	 **/
	@ApiModelProperty(value = "")

	public String getGenero() {
		return genero;
	}

	public void setGenero(String genero) {
		this.genero = genero;
	}

	public Usuario fechaNacimiento(String fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
		return this;
	}

	/**
	 * Get fechaNacimiento
	 * @return fechaNacimiento
	 **/
	@ApiModelProperty(value = "")

	public String getFechaNacimiento() {
		return fechaNacimiento;
	}

	public void setFechaNacimiento(String fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		Usuario usuario = (Usuario) o;
		return Objects.equals(this.documento, usuario.documento) &&
				Objects.equals(this.username, usuario.username) &&
				Objects.equals(this.nombres, usuario.nombres) &&
				Objects.equals(this.apellidos, usuario.apellidos) &&
				Objects.equals(this.genero, usuario.genero) &&
				Objects.equals(this.fechaNacimiento, usuario.fechaNacimiento);
	}

	@Override
	public int hashCode() {
		return Objects.hash(documento, username, nombres, apellidos, genero, fechaNacimiento);
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("class Usuario {\n");

		sb.append("    documento: ").append(toIndentedString(documento)).append("\n");
		sb.append("    username: ").append(toIndentedString(username)).append("\n");
		sb.append("    nombres: ").append(toIndentedString(nombres)).append("\n");
		sb.append("    apellidos: ").append(toIndentedString(apellidos)).append("\n");
		sb.append("    genero: ").append(toIndentedString(genero)).append("\n");
		sb.append("    fechaNacimiento: ").append(toIndentedString(fechaNacimiento)).append("\n");
		sb.append("}");
		return sb.toString();
	}

	/**
	 * Convert the given object to string with each line indented by 4 spaces (except the first line).
	 */
	private String toIndentedString(java.lang.Object o) {
		if (o == null) {
			return "null";
		}
		return o.toString().replace("\n", "\n    ");
	}
}
